module.exports = function(RED){
	function rmseNode(config){
		const utils = require('../../../utils/utils')

		//set configurations
		this.name = 'rmse'
		this.parameters = {}
		utils.run(RED, this, config)
	}

	RED.nodes.registerType("rmse", rmseNode)
}