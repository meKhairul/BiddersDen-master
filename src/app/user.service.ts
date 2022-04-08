import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http"
import { User } from "./user";
@Injectable({
    providedIn: 'root'
})

export class UserService{
    API_URL = 'http://127.0.0.1:8000/api/users/'
    constructor(private http: HttpClient){}
    listUsers(){
        return this.http.get<User>(this.API_URL)
    }
    addUser(data:any){
        return this.http.post<User>(this.API_URL, data)
    }
}