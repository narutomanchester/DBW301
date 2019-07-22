#!/bin/bash

flask db upgrade heads
supervisord
