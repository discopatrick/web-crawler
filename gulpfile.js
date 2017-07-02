var gulp = require('gulp');
var shell = require('gulp-shell');
var connect = require('gulp-connect');

gulp.task('test', shell.task([
  'venv/bin/python -m unittest'
]));

gulp.task('flake8', shell.task([
  'venv/bin/flake8 test/ source/'
]));

gulp.task('autopep8', shell.task([
    'venv/bin/autopep8 source/*.py -i',
    'venv/bin/autopep8 test/*.py -i'
]));

gulp.task('watch', function(){
  gulp.watch(
    [
      './**/*.py',
    ],
    ['flake8', 'test']
  )
})

gulp.task('connect', function() {
  connect.server({
    root: ['test/functional/site']
  });
});

gulp.task('default', ['test']);
