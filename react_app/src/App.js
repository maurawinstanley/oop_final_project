import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import ReactDOM from 'react-dom';

// function App() {
//   const [currentTime, setCurrentTime] = useState(0);

//   useEffect(() => {
//     fetch('/time').then(res => res.json()).then(data => {
//       setCurrentTime(data.time);
//     });
//   }, []);

//   return (
//     <div classURL ="App">
//       <header classURL ="App-header">

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
                  url: ''};

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
      this.setState({url: json[0]})
      })
  }

  

  render() {
    // const recycleStyle = {
    //   backgroundColor: 'blue',
    // };
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

ReactDOM.render(<App />, document.getElementById('root'));
export default App;

