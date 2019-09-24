import React from 'react';
import axios from 'axios';
import {connect} from 'react-redux';
import Bursts from '../components/Burst';
import BurstForm from '../components/BurstForm';




class BurstList extends React.Component {
    
    state = {
        bursts: [],
        userprofiles: [],
        users: []
    }

    fetchBursts = () => {
        axios.get('http://34.222.26.155:8080/api/bursts/')
            .then(res => {
                this.setState({
                    bursts: res.data
                });
            });
    }

    fetchUserProfiles = () => {
        axios.get('http://34.222.26.155:8080/api/userprofiles/')
            .then(res => {
                this.setState({
                    userprofiles: res.data
                });
            });
    }

    fetchUsers = () => {
        axios.get('http://34.222.26.155:8080/api/users/')
            .then(res => {
                this.setState({
                    users: res.data
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
            this.fetchUserProfiles();
            this.fetchUsers();
            
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
                    <div >
                            {this.state.bursts.map(burst => (
                                <div style={{ marginBottom: 10, borderRadius: 5, padding: 10, background: '#fff'}}>
                                
                                { burst.author != null &&
                                <div>
                                <img src={ burst.author.picture } style={{ objectFit: "cover", objectPosition: "50% 0", width: 40, height: 40, borderRadius: "50%"}} /> 
                                
                                <b>  {burst.author.displayname}</b> <small><b>@{burst.author.user.username}</b></small> <small> {burst.timestamp}</small>
                                </div>
                                }
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