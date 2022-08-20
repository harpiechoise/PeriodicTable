import os


def get_asset_path(asset_name, folder='img'):
    return os.path.join(os.getcwd(),
                        "assets",
                        folder,
                        asset_name)
