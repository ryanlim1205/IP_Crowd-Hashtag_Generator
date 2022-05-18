import React, {useContext, useState} from 'react';
import "./Slide.css"
import App, { AppContext } from '../App';

function Slide() {
    const [hashtags, setHashtags] = useState('')
    const [state, setState, sentence, setSentence] = useContext(AppContext)


    const handleFormValueChange = (value) => {
        setSentence(value)
    }

    const Body = () => {
        switch (state) {
            case ("open") : return <div> <h1 className='header-text'> HASHTAG GENERATOR </h1> <h1 className='bighash'>#</h1> </div>
            case ("type") : return <input className='type-bar' type='text' 
                defaultValue={sentence} 
                onChange={(e) => {
                    handleFormValueChange(e.currentTarget.value)
                }}
                placeholder="generate hashtags" 
                />
            case ("return") : return <h1 className='header-text'> #hashtags </h1>
        }
    }


    return ( <div className="Slide">
        <Body />
        <p>{hashtags}</p>
    </div> );
}

export default Slide;