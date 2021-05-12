import { Component, OnInit, Input } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms'; 

import { Location } from '@angular/common';
import { RegisterServiceService } from 'src/app/register-service.service';
import { Register } from './../../models/Register';
import {Router } from '@angular/router'

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  @Input() data : Register = {name: '', password: '', email: ''}



  formGroup !: FormGroup; 

  constructor(private registerService: RegisterServiceService,  private location: Location, private router: Router ) { }

  ngOnInit(): void {
    this.initForm();
  }
  save(): void {
    this.registerService.register(this.data).subscribe(res => this.router.navigate(['/login']));
  }
  // goBack(): void {
  //   this.location.back();
  // }
  initForm() {
    this.formGroup = new FormGroup({
      name: new FormControl('', [Validators.required]),
      email: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required])
    })
  }
  

}
