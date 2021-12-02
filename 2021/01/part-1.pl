#!/usr/bin/perl

use v5.10;

$previous_line = 'Inf';
$count = 0;
while (<>) {
	if ($previous_line < $_) {
		$count++;
	}
	$previous_line = $_;
}
say $count;
