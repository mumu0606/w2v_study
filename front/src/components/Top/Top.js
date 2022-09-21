import React, { useState } from 'react';
import axios from 'axios';
import TextInput from 'react-autocomplete-input';
// import { SimilarContext } from '../Context/SimilarData';
import { GraphArea } from '../GraphArea/GraphArea'
import { SimilarContext } from '../Context/SimilarData';
import 'react-autocomplete-input/dist/bundle.css';
import Select from 'react-select';
import styled from 'styled-components';
import { selectData } from '../../data/selectData'


// class TextField extends Component {
//     // constructor(props){
//     //   super(props)
//     //   this.state = {
//     //     pokeName: ""
//     //   }
//     // }
//     // render() {
//     //   return <input type="text"
//     //                 onChange={(event) => this.setState({enteredValue: event.target.value})}>
//     //          </input>;
//     // }
//   }

const StyledSelect = styled(Select)`
    position: absolute;
    left: 100px;
    top: 32px;
`

const StyledButton = styled('button')`
    position: absolute;
    left: 110px;
    top: 70px;
`

const StyledLabel = styled('label')`
    position: absolute;
    left: 250px;
    top: 70px;
`

// SelectのStyleを設定
const customStyles = {
    option: (provided, state) => ({
      ...provided,
      //ここでボックスの中身のスタイルをカスタマイズ
      borderBottom: "1px dotted pink",
      color: state.isSelected ? "red" : "blue",
      padding: 2,
    }),
    control: () => ({
      // none of react-select's styles are passed to <Control />
      //ここでボックス自体のスタイルをカスタマイズ
      top: 100,
      left: 200,
      width: 300,
      display: "flex",
    }),
    singleValue: (provided, state) => {
      const opacity = state.isDisabled ? 0.5 : 1;
      const transition = "opacity 300ms";

      return { ...provided, opacity, transition };
    },
}

const SimilarData = React.createContext({})

export default function TextField() {
    let backEndURL = 'http://localhost:8000/similar?name='
    const [pokeName, setPokeName] = useState("")
    const [pokeData, setPokeData] = useState({})
    console.log(Object.keys(pokeData).length)
    const setURL = (graphMode) => {
        backEndURL = 'http://localhost:8000/similar?name='
        if (graphMode === 'type_mode') {
            console.log('break')
            backEndURL = 'http://localhost:8000/similar_with_type?name='
        }
    }
    const callAPI = (pokeName) => {
        console.log(backEndURL)
      axios.get(backEndURL + pokeName).then((response) => {
          setPokeData(response.data)
      })
    }
  

    return (
        <div>
            <StyledSelect
                styles={customStyles}
                width='200px'
                options={selectData}
                isMulti
                onChange={(value) => {
                    console.log(value[0].value)
                    setPokeName(value[0].value)}
                }
            />
            <StyledButton onClick={() => callAPI(pokeName)}>グラフ表示</StyledButton>
            <StyledLabel>
                <input type="radio" value="type_mode" onChange={(e) => setURL(e.target.value)}></input>
                type_mode
            </StyledLabel>
            { Object.keys(pokeData).length &&
                <SimilarContext.Provider value={pokeData}>
                    <GraphArea></GraphArea>
                </SimilarContext.Provider>
            }
        </div>
    )
}