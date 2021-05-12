import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Register } from '../app/models/Register';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class RegisterServiceService {

  private registerURL = 'http://localhost:5000'

  constructor(private http:HttpClient) { }

  // register(data: Todo) {
  //   return this.http.post(this.registerURL + '/users', data)
  // }
  register(data: Register) {
    //console.log(data);
      return this.http.post(this.registerURL + '/user', data, httpOptions)
    }

}
