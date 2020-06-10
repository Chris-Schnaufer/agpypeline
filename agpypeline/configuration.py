"""COnfiguration information for an AgPipeline Transformer
"""

class Configuration:
    """Class instance for Transformer configuration information
    """
    # The version number of the transformer
    transformer_version = None

    # The transformer description
    transformer_description = None

    # Short name of the transformer
    transformer_name = None

    # The sensor associated with the transformer
    transformer_sensor = None

    # The transformer type (eg: 'rgbmask', 'plotclipper')
    transformer_type = None

    # The name of the author of the extractor
    author_name = None

    # The email of the author of the extractor
    author_email = None

    # Contributors to this transformer
    contrubutors = []

    # Reposity URI of where the source code lives
    repository = None
