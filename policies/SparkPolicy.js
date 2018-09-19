const exec = require('child_process').exec;

module.exports = {
	/**
	 * @name sparkSubmit
	 * @description spark 앱을 실행
	 * @method 
	 * @param {String} req.user.email - 유저 이메일
	 * @param {String} req.body.App - 선택한 앱
	 * @param {String} req.body.data - 선택한 데이터 파일
	 * @param {String} req.body.parameter - 입력한 파라미터
	 */
	sparkSubmit(req, res, next) {
		const email = req.user.email
		const submit = 'spark-submit '+'--name '+email+' ../app/'+req.body.APP+' --file='+req.body.data + ' ' +  req.body.parameter
		exec(submit, function (err, stdout, stderr) {
			console.log(submit)
			if(err !== null) {
				console.log('exec error :' + err)
				res.send({status: false, result:"error"})
			}
			else {
				req.body.stdout = stdout
				next()
			}
		});
	}
}

