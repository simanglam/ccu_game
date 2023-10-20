import './App.css';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css'
import axios from 'axios'

function App() {
  const BASEURL = "https://4b0d-2001-b400-e606-494e-3440-e668-928d-200d.ngrok-free.app"
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
