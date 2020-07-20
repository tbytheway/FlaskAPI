import React, { Component } from 'react';
import axios from 'axios'
import RenderMovies from './render-movies';

export default class App extends Component {
   constructor() {
        super()
          this.state = {
            movies: []
          }

        this.componentDidMount = this.componentDidMount.bind(this)
    }

    renderMovies() {
      return this.state.movies.map(movie => {
        return (
          <div key={movie.id}>
          <RenderMovies
            title={movie.title}
            actors={movie.actors}  
          />
          </div>
        )
      })
    }
  
    
      componentDidMount() {
        axios.get("http://localhost:5000/movies")
        .then(res => {
          this.setState({
            movies: res.data
          })
        })
      }


     class SubmitForm extends Component {
        state = {
        name: '',
  };
/* This is where the magic happens 
*/
handleSubmit = event => {
    event.preventDefault();
    const movie = {
      name: this.state.movie
    }
    axios.post('http://localhost:5000/movie', { movie })
      .then(res=>{
        console.log(res);
        console.log(res.data);
        window.location = "/retrieve" //This line of code will redirect you once the submission is succeed
      })
  }
handleChange = event =>{
    this.setState({ movie: event.target.value});
  }
render() {;
      
    
  render() {
    return (
      <div className='app'>
       <h1>Movie App</h1>
       {this.renderMovies()}
       <form>
         <h3>Input new movie</h3>
         <form onSubmit = { this.handleSubmit }>
          <label> Person Name:
            <input type = "text" name = "movie" onChange= {this.handleChange}/>
          </label>
          <button type = "submit"> Add </button>
        </form>
         <input type="text" placeholder='Title'/>
         <input type="text" placeholder='Actors'/>
       </form>
       
        
      </div>
    );
  }
}
