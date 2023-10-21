import './App.css';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'

function App() {
  const BASEURL = window.location.href

  const handleClick = () => {
    axios.post(BASEURL).then().then()
  }
  return (
    <div className='App-header'>
      <div className='transformed'>
        <Button variant = "danger" onClick={handleClick}>擲骰</Button>
      </div>
    </div>
  );
}

export default App;
