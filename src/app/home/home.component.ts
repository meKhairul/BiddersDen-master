import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Emitters } from '../emiiters/Emitter';
import { ProductService } from '../product.service';
import { Product } from '../product';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  userdata!: any;
  products: Product[]=[];
  constructor(private userService:UserService,private productService:ProductService,private router:Router) { }

  ngOnInit(): void {
    this.authenticate();
    this.products = this.productService.getProducts();
  }
  authenticate(){
    this.userService.authenticate().subscribe(response => {
      this.userdata = response;
      this.userService.setUser(this.userdata);
      //alert("Logged In as .. " + String(this.userdata.username) )
      Emitters.authEmitter.emit(true);
    },
    err => {
      //alert("not Logged In")
      Emitters.authEmitter.emit(false);
    }
  );
  }

  showProduct(product:Product){
    this.productService.setProductToBeShown(product);
    this.router.navigate(['product']);
  }

}
