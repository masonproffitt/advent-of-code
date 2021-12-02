#!/usr/bin/perl

use v5.10;
use List::Util qw(sum);

@sliding_window = ('Inf', 'Inf', 'Inf');
$count = 0;
$previous_total = 'Inf';
while (<>) {
	shift @sliding_window;
        push @sliding_window, $_;
        $current_total = sum @sliding_window;
	if ($previous_total < $current_total) {
		$count++;
	}
	$previous_total = $current_total;
}
say $count;
