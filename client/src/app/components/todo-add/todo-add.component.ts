
import { Component, OnInit, Input } from '@angular/core';
import { Location } from '@angular/common';
import { FormGroup, Validators, FormBuilder} from '@angular/forms'
import { Todo } from './../../models/Todo';
import { TodoService } from './../../todo.service';

@Component({
  selector: 'app-todo-add',
  templateUrl: './todo-add.component.html',
  styleUrls: ['./todo-add.component.css']
})
export class TodoAddComponent implements OnInit {

  @Input() todo : Todo = {title: '', content: ''}

  

  constructor(private todoService: TodoService, private location: Location) { }
  
  ngOnInit(): void {
    // this.form = this.fb.group({
    //   title: ['', [Validators.required]],
    //   content: ['', [Validators.required, Validators.minLength(5), Validators.maxLength(12)]]
    // });
  }

  save(): void {
    this.todoService.addTodo(this.todo).subscribe(() => this.goBack());
  }

  goBack(): void {
    this.location.back();
  }
  

}
