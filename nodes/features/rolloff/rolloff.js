module.exports = function(RED){
	function rolloffNode(config){
		const utils = require('../../../utils/utils')

		//set configurations
		this.name = 'rolloff'
		this.parameters = {}
		utils.run(RED, this, config)
	}

	RED.nodes.registerType('rolloff', rolloffNode)
}
