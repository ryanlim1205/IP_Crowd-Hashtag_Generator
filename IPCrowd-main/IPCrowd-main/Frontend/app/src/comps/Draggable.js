import React, { useContext, useState } from 'react';
import "./Draggable.css"
import { AppContext } from '../App';

function Draggable() {
    const [btnText, setBtnText] = useState("GET STARTED")
    const [state, setState, sentence, setSentence] = useContext(AppContext)
    let history = ["i ate today", "georgia tech", "my supper was great"]

    const toggleDragged = () => {
        if (state == "type") {
            if (sentence == "") {
                document.getElementsByClassName('Draggable')[0].classList.remove('vertTranslateUp')    
                document.getElementsByClassName('Draggable')[0].classList.add('vertTranslateDown')
                setBtnText("GET STARTED")
                setState("open")
            } else {
                document.getElementsByClassName('Draggable')[0].classList.remove('vertTranslateUp')    
                document.getElementsByClassName('Draggable')[0].classList.add('vertTranslateDown')
                setBtnText("GENERATED")
                setState("return")
            }
            
        } else {
            if (document.getElementsByClassName('Draggable')[0].classList.contains('vertTranslateDown')) {
                document.getElementsByClassName('Draggable')[0].classList.remove('vertTranslateDown')
            }
            document.getElementsByClassName('Draggable')[0].classList.add('vertTranslateUp')
            setBtnText("RETURN")
            setState("type")
        }
    }

    const handleReturnButton = () => {
        if (sentence != "" && state == 'type') {
            console.log(sentence)
            setState("return")
            async function getBackend() {
            const res = await fetch('http://localhost:5000/gethash', {
                method: 'POST',
                headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json' ,
                },
                body: JSON.stringify(sentence),
                mode: 'cors'
            }
            ).then((x) => x.json()).then((y) => console.log(y))
            }
            getBackend()
        }
        toggleDragged()
    }

    const handleHistoryClick = (value) => {
        setSentence(sentence + value)
    }

    return ( <div className='Draggable'>
        <div className='tab' >
            <button className='drag-button' onClick={toggleDragged}>{ (state == "type") ? "|||" : "=" }</button>
        </div>
        <div className='content'>
            <button className='return-button' onClick={handleReturnButton}>{btnText}</button>
            {history.map((v) => {return <button className='each-sentence' onClick={(e) => handleHistoryClick(v)} >{"⏰ " + v}</button>})}
            
        </div>
    </div> );
}

export default Draggable;