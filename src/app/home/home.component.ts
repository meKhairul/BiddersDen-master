import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Emitters } from '../emiiters/Emitter';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  userdata!: any;

  constructor(private userService:UserService) { }

  ngOnInit(): void {
    this.authenticate();
  }
  authenticate(){
    this.userService.authenticate().subscribe(response => {
      this.userdata = response
      alert("Logged In as .. " + String(this.userdata.username) )
      Emitters.authEmitter.emit(true);
    },
    err => {
      alert("not Logged In")
      Emitters.authEmitter.emit(false);
    }
  );
  }

}
