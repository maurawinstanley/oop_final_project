import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';

// function App() {
//   const [currentTime, setCurrentTime] = useState(0);

//   useEffect(() => {
//     fetch('/time').then(res => res.json()).then(data => {
//       setCurrentTime(data.time);
//     });
//   }, []);

//   return (
//     <div className="App">
//       <header className="App-header">

//         ... no changes in this part ...

//         <p>The current time is {currentTime}.</p>
//       </header>
//     </div>
//   );
// }

// export default App;


class App extends React.Component {

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
          URL to Classify
          <input type="text" name="url"/>
          <input type="submit" onChange={this.handleChange} value={this.state.value} />
        </label>
      </form>
        
      </div>
    );
  }
}


export default App;

