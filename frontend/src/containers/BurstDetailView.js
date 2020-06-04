import React from 'react';
import axios from'axios';
import {connect} from 'react-redux';
import { Card } from 'antd';
import '../style.css';

class BurstDetail extends React.Component {
    
    state = {
        burst: {}
    }

    componentWillReceiveProps(newProps) {
        console.log(newProps);
        if(newProps.token) {
            axios.defaults.headers = {
                "Content-Type": "application/json",
                Authorization: newProps.token
            }
            const burstID = this.props.match.params.burstID;
            axios.get(`http://34.222.26.155:8080/api/bursts/${burstID}/`)
            .then(res => {
                this.setState({
                    burst: res.data
                });
            })
        }   
    }

    handleDelete = (event) => {
        event.preventDefault();
        if (this.props.token !== null) {
            const burstID = this.props.match.params.burstID;
            axios.defaults.headers = {
                "Content-Type": "application/json",
                Authorization: this.props.token
            }
            axios.delte(`http://34.222.26.155:8080/api/${burstID}/`);
            this.props.history.push('/');
            this.forceUpdate();
        } else {
            //show some kind of message
        }
        
    }
    
    render() {
        return (
            <Card title={this.state.burst.title}>
                <p>{this.state.burst.bodytext}</p>
            </Card>
        )
    }
}

const mapStateToProps = state => {
    return {
      token: state.token
    }
  }

export default connect(mapStateToProps)(BurstDetail);