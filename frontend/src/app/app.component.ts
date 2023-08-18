import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import  { Customer }  from './data/customer';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})


export class AppComponent {


  constructor(private http: HttpClient) {}

  title = 'frontend';
  customers: Customer[] = [];
  public firstName: string = "";
  public description: string = "";

  onClick() {
    this.customers = [];
    const test = this.http.get("http://localhost:3000");
    test.subscribe(users => {
      for (let [_, value] of Object.entries(users)) {
        const customer: Customer = {
          firstname: value[0],
          test: value[1]
        }
        this.customers.push(customer);
      }
    });
  }

  onSubmit() {
    if (this.firstName == "") {
      window.alert("First name cannont be empty");
      return
    }
    const postData = {name: this.firstName, description: this.description};
    console.log(postData);
    this.http.post<any>('http://localhost:3000/customer', postData).subscribe(data => {})
    this.firstName = "";
    this.description = "";
  }
}




