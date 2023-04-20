const Workweek = 5;
const WorkYear = 53;
// FETCH and READ the people.json disk file

fetch('./people.json')
  .then(response => response.json())
  .then(data => {
    // Loop through an array in the JSON file and log to console
    data.forEach(person => {
      console.log(getFullName(person));
      console.log(getAge(person));
      console.log(`Their Salary is around $${Salary(person)}`);
      console.log(genderjob(person));
    });
  })
  .catch(error => {
    // Handle any errors that occur while fetching the file
    console.error(error);
  });
// Function to detrmine statement outputted
  function genderjob(person) {
    switch(person.gender){
      case "female": 
        return`${person.firstname} is a female and works as ${person.Job}`;
        break;
      case "male":
        return `${person.firstname} is a male and works as ${person.Job}`;
        break;
      default:
        return `${person.firstname} works as ${person.Job}`;
    }
  }
//function to combine name
  function getFullName(person) {
    return `${person.firstname} ${person.lastname}`;
  }
//get age
  function getAge(person) {    
    return `${person.firstname} is ${new Date().getFullYear() - 
      new Date(person.birthday).getFullYear()} years old.`; 
  }
//get gender
  function getGender(person){
    return person.gender;
  }
//get wage
  function getWage(person){
    return person.Wage;
  }
//calculate salary
  function Salary(person){
    return (((person.wage * 8) * Workweek) * WorkYear)
  }

//output same info to html file
const logsDiv = document.getElementById("logs");


fetch("people.json")
  .then((res) => res.json())
  .then((data) => {
    data.forEach((person) => {
      logsDiv.innerHTML += `<p>${getFullName(person)}</p>`;
      logsDiv.innerHTML += `<p>${getAge(person)}</p>`;
      logsDiv.innerHTML += `<p>Their Salary is around $${Salary(person)}</p>`;
      logsDiv.innerHTML += `<p>${genderjob(person)}</p>`;
    });
});