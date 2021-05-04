
import { Component, OnInit, Input } from '@angular/core';
import { Location } from '@angular/common';
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
  }

  save(): void {
    this.todoService.addTodo(this.todo).subscribe(() => this.goBack());
  }

  goBack(): void {
    this.location.back();
  }

}
