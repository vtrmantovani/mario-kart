### Set up
1.  Create a virtualenv with python 3.6:

    ```
    virtualenv -p python3 .venv
    ```

2.  Active the virtualenv:

    ```
    source .venv/bin/activate
    ```

3. Install the Python dependencies:

    ```
    make requirements-dev
    ```

### Create release

1.  Make sure the [`CHANGELOG.md`](https://github.com/vtrmantovani/mario-kart/blob/master/CHANGELOG.md) is up to date with changes made by approved PRs since the last release.

2.  According to the changes made in the project, define which version will be published and run:

    ```
    - `make release-patch` If they are small changes or bugfixes
    - `make release-minor` If new features are changed or have major changes
    - `make release-major` If the changes show compatibility breaches with previous versions
    ```

    * For more information, read documentation [semantic versioning](http://semver.org/)

3. Update master with updated changelog and new generated tag:

    ```
    git push
    git push --tags
    ```

4. On [`github`](https://github.com/vtrmantovani/mario-kart/releases), edit the newly released release and update it with the version information on [`CHANGELOG.md`](https://github.com/vtrmantovani/mario-kart/blob/master/CHANGELOG.md).