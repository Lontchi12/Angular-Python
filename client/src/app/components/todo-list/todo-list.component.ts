
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Todo } from './../../models/Todo';
import { TodoService } from './../../todo.service';


@Component({
  selector: 'app-todo-list',
  templateUrl: './todo-list.component.html',
  styleUrls: ['./todo-list.component.css']
})
export class TodoListComponent implements OnInit {

  todos: Todo[] = [];

  constructor(private route: ActivatedRoute, private todoService: TodoService) { }

  ngOnInit(): void {

    this.getTodos();
  }

  getTodos(): void {
		this.todoService.getTodos().subscribe(todos => this.todos = todos);
	}

	delete(todo: Todo): void {
		this.todoService.deleteTodo(todo).subscribe(success=> {this.getTodos();});
	}

}
