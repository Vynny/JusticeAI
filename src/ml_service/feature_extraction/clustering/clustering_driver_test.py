import unittest
from feature_extraction.clustering import clustering_driver
from util.constant import Path

Path.raw_data_directory = Path.test_data_directory


class TestClustering(unittest.TestCase):
    def test_kmeans(self):
        # k-means
        command_list = ["--kmeans", "--fact", "1"]
        self.assertTrue(clustering_driver.run(command_list))

        command_list = ["--kmeans", "--decision", "1"]
        self.assertTrue(clustering_driver.run(command_list))

        command_list = ["--kmeans", "--dwdw", "1"]
        self.assertTrue(not clustering_driver.run(command_list))

        command_list = ["--kmeans", "--decision", "string"]
        self.assertTrue(not clustering_driver.run(command_list))

    def test_dbscan(self):
        # dbscan
        command_list = ["--dbscan", "--fact", "1", "1"]
        self.assertTrue(clustering_driver.run(command_list))

        command_list = ["--dbscan", "--decision", "1", "1"]
        self.assertTrue(clustering_driver.run(command_list))

        command_list = ["--dbscan", "--dwdw", "1"]
        self.assertTrue(not clustering_driver.run(command_list))

        command_list = ["--dbscan", "--decision", "string"]
        self.assertTrue(not clustering_driver.run(command_list))

    def test_hdbscan(self):
        # dbscan
        command_list = ["--hdbscan", "--fact", "2", "1"]
        self.assertTrue(clustering_driver.run(command_list))

        command_list = ["--hdbscan", "--decision", "2", "1"]
        self.assertTrue(clustering_driver.run(command_list))

        command_list = ["--hdbscan", "--dwdw", "1"]
        self.assertTrue(not clustering_driver.run(command_list))

        command_list = ["--hdbscan", "--decision", "string"]
        self.assertTrue(not clustering_driver.run(command_list))

    def test_random_command(self):
        # bad command
        command_list = ["-random"]
        self.assertTrue(not clustering_driver.run(command_list))

        command_list = ["-random", 'ranndom']
        self.assertTrue(not clustering_driver.run(command_list))