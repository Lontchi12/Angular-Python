import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms'; 
import { ReactiveFormsModule } from '@angular/forms';
import { AuthServiceService } from 'src/app/auth-service.service';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { Router } from '@angular/router';
import { Login } from './../../models/Login';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  // @Input() data : Login = {name: '', password: ''}


  form!: FormGroup; 
  
  constructor(private authService: AuthServiceService, private formBuilder: FormBuilder, private http: HttpClient, private router: Router ) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      name: '',
      password: ''
    })
  }
  httpOptions = {
    headers: new HttpHeaders({
      'Accept': 'text/plain',
      'Content-Type': 'text/plain'
    })
  };

  submit():void {
    let data = JSON.stringify(this.form.value);
    console.log(data);
    this.http.post<any>('http://localhost:5000/api/login', data,this.httpOptions).subscribe({
      next: data => {
          console.log(data);
      },
      error: error => {
          console.error('There was an error!', error);
      }
  })
    // this.http.post('http://localhost:5000/api/login', '',this.httpOptions).subscribe(() => this.router.navigate(['/login']))
  }


  // loginProcess(){
  //   if (this.formGroup.valid){
  //     this.authService.login(this.formGroup.value).subscribe(result => {
  //       if (result.success) {
  //         console.log(result);
  //         alert(result.message);
  //       } else {
  //         alert(result.message)
  //       }
  //     })
  //   }
  // }


}
