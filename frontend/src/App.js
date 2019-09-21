import React, { Component } from 'react';
import 'antd/dist/antd.css';

import CustomLayout from './containers/Layout';
import BurstList from './containers/BurstListView';

class App extends Component {
  render() {
    return (
      <div className="App">
        <CustomLayout>
          <BurstList />
        </CustomLayout>
      </div>
    );
  }
}

export default App;
