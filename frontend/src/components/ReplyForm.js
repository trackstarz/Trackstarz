import React from 'react';
import { Form, Input, Button } from 'antd';
import { connect } from 'react-redux';
import axios from 'axios';

class ReplyForm extends React.Component {
  handleFormSubmit = (event, requestType, replyID) => {
    event.preventDefault();
    const content = event.target.elements.bodytext.value;
    const author = event.target.elements.author.value;
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: this.props.token
    }
    switch (requestType) {
      case 'post':
        return axios.post('http://34.222.26.155:8080/api/replies/', {
          author: author,
          content: content
        })
          .then(res => console.log(res))
          .catch(error => console.error(error));
      case 'put':
        return axios.put(`http://34.222.26.155:8080/api/replies/${replyID}/`, {
          author: author,
          content: content
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
        <Form onSubmit={(event) => this.handleFormSubmit(
          event,
          this.props.requestType,
          this.props.replyID
        )}>
          <Form.Item>
            <Input name="author" placeholder="Enter your name" />
          </Form.Item>
          <Form.Item>
            <Input name="bodytext" placeholder="Tell us what is going on..." />
          </Form.Item>
          <Form.Item>
            <Button type="primary" htmlType="submit">{this.props.btnText}</Button>
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

export default connect(mapStateToProps)(ReplyForm);
