# Build and test
make build && make test

# Deploy to PyPI
make publish

# Run in production
docker run geometry_toolkit sphere --radius 5 --unit m
