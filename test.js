class Employee{
    constructor(firstName, lastName, salary){
        this.firstName = firstName;
        this.lastName = lastName;
        this.salary = salary;
    }
    fullName(){
        console.log(this.firstName,this.lastName)
    }
}

let employee = new Employee('Nick', "C", 1)

employee.fullName();
console.log(Math.floor(10.19))