const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;

//middleware
app.use(express.static('src'));



app.get('/', (req, res)=>{
    res.send("hello")
})

app.listen(PORT, ()=> {
    console.log(`Server running on port ${PORT}`) 
})
