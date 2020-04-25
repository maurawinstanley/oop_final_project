import React from 'react';
//import './App.css';
import URL_handler from './components/url_input'
import 'bootstrap/dist/css/bootstrap.min.css';

import React, { useState, useEffect } from 'react';
import { Form, Input, Button } from 'semantic-ui-react';
// function App() {
//   return (
//     <div className="App">
//       <URL_handler />
//     </div>
//   );
// }

// export default App;



// function App() {
//   const [currentTime, setCurrentTime] = useState(100);

//   useEffect(() => {
//     fetch('/classify').then(res => res.json()).then(data => {
//       setCurrentTime(data.time);
//       console.log(data.time);
//     });
//   }, []);

//   return (
//     <div className="App">
//       <header className="App-header">

//         ... no changes in this part ...

//         <p>The current time is {10}.</p>
//       </header>
//     </div>
//   );
// }

// export default App;


function App() {

 constructor(props) {
    super(props);
    this.state = {value: '',
                  playerName: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    console.log("making request")
    fetch('/result')
      .then(response => {
        console.log(response)
        return response.json()
      })
      .then(json => {
      console.log=(json)
      this.setState({playerName: json[0]})
      })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleSubmit} action="http://localhost:5000/result" method="get">
        <label>
          Player ID:
          <input type="text" name="player_id"/>
          <input type="submit" onChange={this.handleChange} value={this.state.value} />
        </label>
      </form>
        <h1> Player Name: {this.state.playerName} </h1>
      </div>
    );
  }
}


export default App;















