import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Login } from '../app/models/Login';

@Injectable({
  providedIn: 'root'
})
export class AuthServiceService {


    private baseURL = 'http://localhost:5000'

  constructor(private http:HttpClient) { }

  login(data: Login):Observable<any>{
    console.log("The server is ready")
    return this.http.post(this.baseURL +'/login', data, {
      withCredentials:true
    })
  }
  
  // login(): Observable<Login[]> {
   
  //   return this.http.get<Login[]>(this.baseURL + '/login')
  // }
}
