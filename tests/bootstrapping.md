# Bootstrapping
## Bootstrapping the metamodel

`metamodel.py` needs to be updated whenever changes are made to the metamodel (`meta.yaml`). Steps:

1. Make changes to `meta.yaml`, making certian to update the version number.
2. Run the `test_metamodel` unit test in `test_pythongen.py`.  When error free, you will get a comparison error with 
the message `metamodel.py does not match output -- should it be updated?`.  Take a close look at 
`tests/target/metamodel.py` to make sure it is clean, error and lint free.  When it is:
3. Set `update_master` to `True` in the top of `test_pythongen.py` and rerun the test.  You will get an error message
indicating that it is set.
4. Set `update_master` to `False` and run the test one final time.  If you did everything correctly, it should pass.

You can also run the `test_synopsis.py` package to get a summary of the state of affairs. (Note: this will be converted
to a cli entry point at some point in the not too distant future)

## Bootstraping `biolink-model.py`
Follow the same set of instructions above, changing `biolink-model.yaml` and runing the `test_biolinkmodel` in 
`test_pythongen.py`