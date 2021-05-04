

import { Component, OnInit, Input } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { Todo } from './../../models/Todo';
import { TodoService } from './../../todo.service';



@Component({
  selector: 'app-todo-edit',
  templateUrl: './todo-edit.component.html',
  styleUrls: ['./todo-edit.component.css']
})
export class TodoEditComponent implements OnInit {

  @Input() todo!: Todo;

  constructor(private route: ActivatedRoute, private todoService: TodoService, private location: Location) { }

  ngOnInit(): void {
    this.getTodo();
  }
  getTodo(): void {
		const id = + this.route.snapshot.paramMap.get('id')!;
    id && this.todoService.getTodo(id)
		.subscribe(todo => this.todo = todo);
	}

  save(): void {
		this.todoService.updateTodo(this.todo).subscribe(success=> {this.goBack();});
	}

	goBack(): void {
		this.location.back();
	}

}
