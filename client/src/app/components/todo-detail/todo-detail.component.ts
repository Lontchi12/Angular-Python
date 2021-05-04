

import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { Todo } from './../../models/Todo';
import { TodoService } from './../../todo.service';


@Component({
  selector: 'app-todo-detail',
  templateUrl: './todo-detail.component.html',
  styleUrls: ['./todo-detail.component.css']
})
export class TodoDetailComponent implements OnInit {

  todo!: Todo;

  constructor(private route: ActivatedRoute, private todoService: TodoService, private location: Location) { }

  ngOnInit(): void {

    this.getTodo();
  }

  getTodo(): void {
		const id = + this.route.snapshot.paramMap.get('id')!;
    id && this.todoService.getTodo(id)
		.subscribe(todo => this.todo = todo);
	}

//   const id = + this.route.snapshot.paramMap.get('id');
// id && this.studentService.getStudent(id)
//      .subscribe(student => this.SpecificStudent = student);

	goBack(): void {
		this.location.back();
	}

}
