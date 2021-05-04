import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import { Todo } from '../app/models/Todo'

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})
export class TodoService {

  private userUrl = 'http://localhost:5000';  // URL to REST API


  constructor(private http: HttpClient) { }

  /** GET todos from the server */
  getTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>(this.userUrl + '/todos');
  }

  /** GET todo by id. Will 404 if id not found */
  getTodo(id: number): Observable<any> {
    const url = `${this.userUrl}/todo/${id}`;
    return this.http.get<Todo>(url);
  }

  /** POST: add a new todo to the server */
  addTodo(todo: Todo) {
    //console.log(todo);
      return this.http.post(this.userUrl + '/addtodo', todo, httpOptions);
    }

    /** PUT: update the todo on the server */
  updateTodo(todo: Todo): Observable<any> {
    return this.http.put(this.userUrl + '/update', todo, httpOptions);
  }

  /** DELETE: delete the todo from the server */
  deleteTodo(todo: Todo | number) {
	  if (confirm("Are you sure to delete?")) {
		const id = typeof todo === 'number' ? todo : todo.id;
		const url = `${this.userUrl}/delete/${id}`;
		return this.http.delete(url, httpOptions);
	  }
	  return of({});
  }

}
