import React from 'react';
import axios from 'axios';
import {connect} from 'react-redux';
import Bursts from '../components/Burst';
import BurstForm from '../components/BurstForm';




class BurstList extends React.Component {
    
    state = {
        bursts: []
    }

    fetchBursts = () => {
        axios.get('http://34.222.26.155:8080/api/bursts/')
            .then(res => {
                this.setState({
                    bursts: res.data
                });
            });
    }

   

    componentWillReceiveProps(newProps) {
        console.log(newProps);
        if(newProps.token) {
            axios.defaults.headers = {
                "Content-Type": "application/json",
                Authorization: newProps.token
            }
            this.fetchBursts();
            
        }
    }
    
    render() {
        return (
            <div>
                <div style={{ marginBottom: 10, borderRadius: 5, padding: 10, background: '#fff'}}>
                    <BurstForm 
                        requestType="post"
                        burstID={null}
                        btnText="post"/>
                </div>
                    <Bursts data={this.state.bursts}/>
                    <div key={this.state.bursts.id}>
                            {this.state.bursts.map(burst => (
                                <div style={{ marginBottom: 10, borderRadius: 5, padding: 10, background: '#fff'}}>
                                
                                { burst.title != null &&
                                <h2>{burst.title}</h2>
                                }
                                <p>{burst.bodytext}</p>
                                { burst.picture != null &&
                                <img src={burst.picture} width='100%' />
                                }
                                <hr/>
                               </div>
                        
                             ))}
                             
                  
                    </div>
            </div>
        )
    }
}

const mapStateToProps = state => {
    return {
      token: state.token
    }
  }


export default connect(mapStateToProps)(BurstList);