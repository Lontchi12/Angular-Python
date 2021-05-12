
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TodoListComponent } from './components/todo-list/todo-list.component';
import { TodoAddComponent } from './components/todo-add/todo-add.component';
import { TodoEditComponent } from './components/todo-edit/todo-edit.component';
import { TodoDetailComponent } from './components/todo-detail/todo-detail.component';
import { LoginComponent } from './components/login/login.component';
import { RegisterComponent } from './components/register/register.component';
import { HomeComponent } from './components/home/home.component';

const routes: Routes = [
  {path: '', component:HomeComponent},
  {path: 'register', component:RegisterComponent},
  {path: 'login', component:LoginComponent},
  {path: 'todos', component:TodoListComponent},
  {path: 'detail/:id', component:TodoDetailComponent},
  {path: 'edit/:id', component:TodoEditComponent},
  {path: 'addtodo', component:TodoAddComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
