import React from 'react';
import axios from'axios';

import Bursts from '../components/Burst';

const listData = [];
for (let i = 0; i < 23; i++) {
  listData.push({
    href: 'http://ant.design',
    title: `ant design part ${i}`,
    avatar: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png',
    description:
      'Ant Design, a design language for background applications, is refined by Ant UED Team.',
    content:
      'We supply a series of design principles, practical patterns and high quality design resources (Sketch and Axure), to help people create their product prototypes beautifully and efficiently.',
  });
}


class BurstList extends React.Component {
    
    state = {
        bursts: []
    }

    componentDidMount() {
        axios.get('http://34.222.26.155:8080/api/bursts')
        .then(res => {
            this.setState({
                bursts: res.data
            });
            console.log(res.data);
        })

    }
    
    render() {
        return (
            <Bursts data={this.state.bursts}/>
        )
    }
}

export default BurstList;