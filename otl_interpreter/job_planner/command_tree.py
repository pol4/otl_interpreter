class CommandTree(object):

    def __init__(
            self, command,
            previous_command_tree_in_pipeline=None,
            subsearch_command_trees=None,
            awaited_command_trees=None,
            next_command_tree_in_pipeline=None
    ):
        """
        :param command: Command object
        :param previous_command_tree_in_pipeline: Command Tree from  pipeline
        :param subsearch_command_trees: list of commands awaited for dataframe 
        :param awaited_command_trees: awaited list of command trees
        :param next_command_tree_in_pipeline: next Command object for execution
        """
        self.command = command
        self.previous_command_tree_in_pipeline = None
        self.subsearch_command_trees = []
        self.awaited_command_trees = []
        self.next_command_tree_in_pipeline = None

        # if previous command tree in pipeline is None then current command tree is first command tree in pipeline
        self.first_command_tree_in_pipeline = self

        if previous_command_tree_in_pipeline is not None:
            self.set_previous_command_tree_in_pipeline(previous_command_tree_in_pipeline)

        if subsearch_command_trees is not None:
            for subsearch_command in subsearch_command_trees:
                self.add_subsearch_command_tree(subsearch_command)

        if awaited_command_trees is not None:
            for awaited_command_tree in awaited_command_trees:
                self.add_awaited_command_tree(awaited_command_tree)

        if next_command_tree_in_pipeline is not None:
            self.set_next_command_tree_in_pipeline(next_command_tree_in_pipeline)

    def __repr__(self):
        return self.command

    def set_previous_command_tree_in_pipeline(self, previous_command_tree_in_pipeline):
        self.previous_command_tree_in_pipeline = previous_command_tree_in_pipeline
        self.first_command_tree_in_pipeline = previous_command_tree_in_pipeline.first_command_tree_in_pipeline

    def add_subsearch_command_tree(self, subsearch_command_trees):
        self.subsearch_command_trees.append(subsearch_command_trees)

    def add_awaited_command_tree(self, awaited_command_tree):
        self.awaited_command_trees.append(awaited_command_tree)

    def set_next_command_tree_in_pipeline(self, next_command_tree_in_pipeline):
        self.next_command_tree_in_pipeline = next_command_tree_in_pipeline

