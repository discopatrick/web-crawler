var gulp = require('gulp');
var shell = require('gulp-shell');

gulp.task('test', shell.task([
  'python -m unittest'
]));

gulp.task('watch', function(){
  gulp.watch(
    [
      './**/*.py',
    ],
    ['test']
  )
})
