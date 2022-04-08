import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { UserService } from '../user.service';
import { User } from '../user';;
@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  //angForm:FormGroup
  constructor(private fb: FormBuilder, private userService: UserService, private route: Router) { 
    /*this.angForm = this.fb.group({
      name:['', Validators.required],
      phone:['', Validators.required],
      email:['', Validators.required],
      address:['', Validators.required],
      username:['', Validators.required],
      password:['', Validators.required],
    })
    */
  }
  user = new User();

  ngOnInit(): void {
  }

  addUser(){
    console.log("adding User")
    console.log(this.userService.listUsers())
    this.userService.addUser(this.user).subscribe(data=>{
      console.log("added User")
      this.route.navigate(['app-home'])
    })
    console.log("After adding User")
  }
}
