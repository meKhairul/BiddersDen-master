import { Component, OnInit } from '@angular/core';
import { Product } from '../product';
import { ProductService } from '../product.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  productShow = this.productService.getProductToBeShown();
  constructor(private productService:ProductService) { }

  ngOnInit(): void {
  }

  


}
