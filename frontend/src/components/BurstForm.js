import React from 'react';
import { Form, Input, Button } from 'antd';
import {connect} from 'react-redux';

import axios from 'axios';

class BurstForm extends React.Component {
  
    handleFormSubmit = (event, requestType, burstID) => {
        const bodytext = event.target.elements.bodytext.value;
        axios.defaults.headers = {
          "Content-Type": "application/json",
          Authorization: this.props.token
        }
        switch ( requestType ) {
            case 'post':
                return axios.post('http://34.222.26.155:8080/api/bursts/', {
                    author: 8,
                    bodytext: bodytext
                })
                .then(res => console.log(res))
                .catch(error => console.error(error));
            case 'put':
                    return axios.put(`http://34.222.26.155:8080/api/bursts/${burstID}/`, {
                        author: 8,
                        bodytext: bodytext
                    })
                    .then(res => console.log(res))
                    .catch(error => console.error(error));
            default:
              return null;
        }
    }

  render() {
    return (
      <div>
        <h2>Update Status</h2>
        <Form className="burst_inputs" id="burst_form" onSubmit={(event) => this.handleFormSubmit(
            event,
            this.props.requestType,
            this.props.burstID
        )}>
          <Form.Item>
            <Input name="bodytext" placeholder="Tell us what is going on..." />
          </Form.Item>
          <Form.Item>
            <Button id="burst_submit" type="primary" htmlType="submit">{this.props.btnText}</Button>
          </Form.Item>
        </Form>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.token
  }
}

export default connect(mapStateToProps)(BurstForm);
