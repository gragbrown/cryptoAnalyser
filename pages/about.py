import streamlit as st
from pages import utility
import streamlit.components.v1 as components

def app():
    st.write("AboutUs")
    components.html('''<head><link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script></head>
    <body>
<div class="card-container m-2 border border-3 border border-white rounded-3">
    
        <h3>Kartik Garg</h3>
        <h6>Dehradun</h6>
        <p>Software Developer <br/> front-end developer</p>
        <div class="buttons">
            <button class="primary" onclick="window.location.href='https://www.linkedin.com/in/kartik-garg-536a75221';">
                Connect
              </button>
              <button class="primary ghost" onclick="window.location.href='https://github.com/kartikk-garg';">
                Github
              </button>
        </div>
        <div class="skills">
          <h6>Skills</h6>
          <ul>
            <li>Python</li>
            <li>C</li>
            <li>C++</li>
            <li>CSS</li>
            <li>JavaScript</li>
            <li>HTML</li>
            <li>SQL</li>
          </ul>
        </div>
      </div> 
<div class="card-container m-2 border border-3 border border-white rounded-3">
    
    
    <h3>Divyanshu Deoli</h3>
    <h6>Dehradun</h6>
    <p>Software Developer <br/> Back-end developer</p>
    <div class="buttons">
        <button class="primary" onclick="window.location.href='https://www.linkedin.com/in/divyanshu-deoli-7920a3183';">
            Connect
          </button>
          <button class="primary ghost" onclick="window.location.href='https://github.com/divyanshudeoli';">
            Github
          </button>
    </div>
    <div class="skills">
      <h6>Skills</h6>
      <ul>
        <li>C</li>
        <li>C++</li>
        <li>HTML</li>
        <li>CSS</li>
        <li>Python</li>
        <li>SQL</li>
        <li>JavaScript</li>
        <li>Java</li>
      </ul>
    </div>
  </div>

  <div class="card-container m-2 border border-3 border border-white rounded-3">
    
        
    <h3>Tushar Jain</h3>
    <h6>Ghaziabad</h6>
    <p>Software Developer <br/> Back-end developer</p>
    <div class="buttons">
        
        <button class="primary" onclick="window.location.href='https://www.linkedin.com/in/tushar-jain-089672191';">
            Connect
          </button>
          <button class="primary ghost" onclick="window.location.href='https://github.com/tusharja-in';">
            Github
          </button>
    </div>
    <div class="skills">
      <h6>Skills</h6>
      <ul>
        <li>C++</li>
        <li>C</li>
        <li>Java</li>
        <li>Kotlin</li>
        <li>IoT</li>
        <li>Android</li>
        <li>SQL</li>
        <li>Arduino</li>
      </ul>
    </div>
  </div></body>
  <style>
    

@import url('https://fonts.googleapis.com/css?family=Montserrat');

* {
  box-sizing: border-box;
}

h3 {
  margin: 10px 0;
}

h6 {
  margin: 5px 0;
  text-transform: uppercase;
}

p {
  font-size: 14px;
  line-height: 21px;
}

.card-container {
  background-color: #231E39;
  border-radius: 5px;
  box-shadow: 0px 10px 20px -10px rgba(0,0,0,0.75);
  color: #ebebee;
  padding-top: 30px;
  position: relative;
  width: 350px;
  max-width: 100%;
  text-align: center;
}

.card-container .pro {
  color: #231E39;
  background-color: #FEBB0B;
  border-radius: 3px;
  font-size: 14px;
  font-weight: bold;
  padding: 3px 7px;
  position: absolute;
  top: 30px;
  left: 30px;
}

.card-container .round {
  border: 1px solid #03BFCB;
  border-radius: 50%;
  padding: 7px;
}

button.primary {
  background-color: #03BFCB;
  border: 1px solid #03BFCB;
  border-radius: 3px;
  color: #231E39;
  font-family: Montserrat, sans-serif;
  font-weight: 500;
  padding: 10px 25px;
}

button.primary.ghost {
  background-color: transparent;
  color: #02899C;
}

.skills {
  background-color: #1F1A36;
  text-align: left;
  padding: 15px;
  margin-top: 30px;
}

.skills ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.skills ul li {
  border: 1px solid #2D2747;
  border-radius: 2px;
  display: inline-block;
  font-size: 12px;
  margin: 0 7px 7px 0;
  padding: 7px;
}

footer {
    background-color: #222;
    color: #fff;
    font-size: 14px;
    bottom: 0;
    position: fixed;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 999;
}

footer p {
    margin: 10px 0;
}

footer i {
    color: red;
}

footer a {
    color: #3c97bf;
    text-decoration: none;
}


</style>
    ''',height = 1300, width = 380)