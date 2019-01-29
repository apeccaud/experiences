'use strict';

const {h, Component, Color, Text} = require('ink');
const PropTypes = require('prop-types');

class UI extends Component {
	constructor(props) {
		super();
		this.stop = props.stop;
    this.state = {
      history: [],
    };
	}

	componentDidMount() {
		let i = 0;
    this.timer = setInterval(() => {
			if (i >= this.stop) process.exit(0);
			i++;
      this.setState({history: [...this.state.history, <Color green>Log {i}</Color>]});
    }, 300);
	}
	
	componentWillUnmount() {
    clearInterval(this.timer);
  }
	
	render() {
		return (
			<div>
				{this.state.history.map(el => <div>{el}</div>)}
			</div>
		);
	}
}

UI.propTypes = {
	stop: PropTypes.number
};

UI.defaultProps = {
	stop: 10
};

module.exports = UI;
