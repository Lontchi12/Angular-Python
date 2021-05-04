
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TodoListComponent } from './components/todo-list/todo-list.component';
import { TodoAddComponent } from './components/todo-add/todo-add.component';
import { TodoEditComponent } from './components/todo-edit/todo-edit.component';
import { TodoDetailComponent } from './components/todo-detail/todo-detail.component';

const routes: Routes = [
  // {path: '', redirectTo: '/user', pathMatch: 'full'},
  {path: 'todo', component:TodoListComponent},
  {path: 'detail/:id', component:TodoDetailComponent},
  {path: 'edit/:id', component:TodoEditComponent},
  {path: 'addtodo', component:TodoAddComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
