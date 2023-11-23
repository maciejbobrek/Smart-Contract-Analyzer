# Generated from ../SolidityA.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .SolidityAParser import SolidityAParser
else:
    from SolidityAParser import SolidityAParser

# This class defines a complete listener for a parse tree produced by SolidityAParser.
class SolidityAListener(ParseTreeListener):

    # Enter a parse tree produced by SolidityAParser#sourceUnit.
    def enterSourceUnit(self, ctx:SolidityAParser.SourceUnitContext):
        pass

    # Exit a parse tree produced by SolidityAParser#sourceUnit.
    def exitSourceUnit(self, ctx:SolidityAParser.SourceUnitContext):
        pass


    # Enter a parse tree produced by SolidityAParser#pragmaDirective.
    def enterPragmaDirective(self, ctx:SolidityAParser.PragmaDirectiveContext):
        pass

    # Exit a parse tree produced by SolidityAParser#pragmaDirective.
    def exitPragmaDirective(self, ctx:SolidityAParser.PragmaDirectiveContext):
        pass


    # Enter a parse tree produced by SolidityAParser#pragmaName.
    def enterPragmaName(self, ctx:SolidityAParser.PragmaNameContext):
        pass

    # Exit a parse tree produced by SolidityAParser#pragmaName.
    def exitPragmaName(self, ctx:SolidityAParser.PragmaNameContext):
        pass


    # Enter a parse tree produced by SolidityAParser#pragmaValue.
    def enterPragmaValue(self, ctx:SolidityAParser.PragmaValueContext):
        pass

    # Exit a parse tree produced by SolidityAParser#pragmaValue.
    def exitPragmaValue(self, ctx:SolidityAParser.PragmaValueContext):
        pass


    # Enter a parse tree produced by SolidityAParser#version.
    def enterVersion(self, ctx:SolidityAParser.VersionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#version.
    def exitVersion(self, ctx:SolidityAParser.VersionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#versionOperator.
    def enterVersionOperator(self, ctx:SolidityAParser.VersionOperatorContext):
        pass

    # Exit a parse tree produced by SolidityAParser#versionOperator.
    def exitVersionOperator(self, ctx:SolidityAParser.VersionOperatorContext):
        pass


    # Enter a parse tree produced by SolidityAParser#versionConstraint.
    def enterVersionConstraint(self, ctx:SolidityAParser.VersionConstraintContext):
        pass

    # Exit a parse tree produced by SolidityAParser#versionConstraint.
    def exitVersionConstraint(self, ctx:SolidityAParser.VersionConstraintContext):
        pass


    # Enter a parse tree produced by SolidityAParser#importDeclaration.
    def enterImportDeclaration(self, ctx:SolidityAParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityAParser#importDeclaration.
    def exitImportDeclaration(self, ctx:SolidityAParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityAParser#importDirective.
    def enterImportDirective(self, ctx:SolidityAParser.ImportDirectiveContext):
        pass

    # Exit a parse tree produced by SolidityAParser#importDirective.
    def exitImportDirective(self, ctx:SolidityAParser.ImportDirectiveContext):
        pass


    # Enter a parse tree produced by SolidityAParser#importPath.
    def enterImportPath(self, ctx:SolidityAParser.ImportPathContext):
        pass

    # Exit a parse tree produced by SolidityAParser#importPath.
    def exitImportPath(self, ctx:SolidityAParser.ImportPathContext):
        pass


    # Enter a parse tree produced by SolidityAParser#contractDefinition.
    def enterContractDefinition(self, ctx:SolidityAParser.ContractDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#contractDefinition.
    def exitContractDefinition(self, ctx:SolidityAParser.ContractDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#inheritanceSpecifier.
    def enterInheritanceSpecifier(self, ctx:SolidityAParser.InheritanceSpecifierContext):
        pass

    # Exit a parse tree produced by SolidityAParser#inheritanceSpecifier.
    def exitInheritanceSpecifier(self, ctx:SolidityAParser.InheritanceSpecifierContext):
        pass


    # Enter a parse tree produced by SolidityAParser#contractPart.
    def enterContractPart(self, ctx:SolidityAParser.ContractPartContext):
        pass

    # Exit a parse tree produced by SolidityAParser#contractPart.
    def exitContractPart(self, ctx:SolidityAParser.ContractPartContext):
        pass


    # Enter a parse tree produced by SolidityAParser#stateVariableDeclaration.
    def enterStateVariableDeclaration(self, ctx:SolidityAParser.StateVariableDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityAParser#stateVariableDeclaration.
    def exitStateVariableDeclaration(self, ctx:SolidityAParser.StateVariableDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityAParser#fileLevelConstant.
    def enterFileLevelConstant(self, ctx:SolidityAParser.FileLevelConstantContext):
        pass

    # Exit a parse tree produced by SolidityAParser#fileLevelConstant.
    def exitFileLevelConstant(self, ctx:SolidityAParser.FileLevelConstantContext):
        pass


    # Enter a parse tree produced by SolidityAParser#customErrorDefinition.
    def enterCustomErrorDefinition(self, ctx:SolidityAParser.CustomErrorDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#customErrorDefinition.
    def exitCustomErrorDefinition(self, ctx:SolidityAParser.CustomErrorDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#typeDefinition.
    def enterTypeDefinition(self, ctx:SolidityAParser.TypeDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#typeDefinition.
    def exitTypeDefinition(self, ctx:SolidityAParser.TypeDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#usingForDeclaration.
    def enterUsingForDeclaration(self, ctx:SolidityAParser.UsingForDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityAParser#usingForDeclaration.
    def exitUsingForDeclaration(self, ctx:SolidityAParser.UsingForDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityAParser#usingForObject.
    def enterUsingForObject(self, ctx:SolidityAParser.UsingForObjectContext):
        pass

    # Exit a parse tree produced by SolidityAParser#usingForObject.
    def exitUsingForObject(self, ctx:SolidityAParser.UsingForObjectContext):
        pass


    # Enter a parse tree produced by SolidityAParser#usingForObjectDirective.
    def enterUsingForObjectDirective(self, ctx:SolidityAParser.UsingForObjectDirectiveContext):
        pass

    # Exit a parse tree produced by SolidityAParser#usingForObjectDirective.
    def exitUsingForObjectDirective(self, ctx:SolidityAParser.UsingForObjectDirectiveContext):
        pass


    # Enter a parse tree produced by SolidityAParser#userDefinableOperators.
    def enterUserDefinableOperators(self, ctx:SolidityAParser.UserDefinableOperatorsContext):
        pass

    # Exit a parse tree produced by SolidityAParser#userDefinableOperators.
    def exitUserDefinableOperators(self, ctx:SolidityAParser.UserDefinableOperatorsContext):
        pass


    # Enter a parse tree produced by SolidityAParser#structDefinition.
    def enterStructDefinition(self, ctx:SolidityAParser.StructDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#structDefinition.
    def exitStructDefinition(self, ctx:SolidityAParser.StructDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#modifierDefinition.
    def enterModifierDefinition(self, ctx:SolidityAParser.ModifierDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#modifierDefinition.
    def exitModifierDefinition(self, ctx:SolidityAParser.ModifierDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#modifierInvocation.
    def enterModifierInvocation(self, ctx:SolidityAParser.ModifierInvocationContext):
        pass

    # Exit a parse tree produced by SolidityAParser#modifierInvocation.
    def exitModifierInvocation(self, ctx:SolidityAParser.ModifierInvocationContext):
        pass


    # Enter a parse tree produced by SolidityAParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:SolidityAParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:SolidityAParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#functionDescriptor.
    def enterFunctionDescriptor(self, ctx:SolidityAParser.FunctionDescriptorContext):
        pass

    # Exit a parse tree produced by SolidityAParser#functionDescriptor.
    def exitFunctionDescriptor(self, ctx:SolidityAParser.FunctionDescriptorContext):
        pass


    # Enter a parse tree produced by SolidityAParser#returnParameters.
    def enterReturnParameters(self, ctx:SolidityAParser.ReturnParametersContext):
        pass

    # Exit a parse tree produced by SolidityAParser#returnParameters.
    def exitReturnParameters(self, ctx:SolidityAParser.ReturnParametersContext):
        pass


    # Enter a parse tree produced by SolidityAParser#modifierList.
    def enterModifierList(self, ctx:SolidityAParser.ModifierListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#modifierList.
    def exitModifierList(self, ctx:SolidityAParser.ModifierListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#eventDefinition.
    def enterEventDefinition(self, ctx:SolidityAParser.EventDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#eventDefinition.
    def exitEventDefinition(self, ctx:SolidityAParser.EventDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#enumValue.
    def enterEnumValue(self, ctx:SolidityAParser.EnumValueContext):
        pass

    # Exit a parse tree produced by SolidityAParser#enumValue.
    def exitEnumValue(self, ctx:SolidityAParser.EnumValueContext):
        pass


    # Enter a parse tree produced by SolidityAParser#enumDefinition.
    def enterEnumDefinition(self, ctx:SolidityAParser.EnumDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#enumDefinition.
    def exitEnumDefinition(self, ctx:SolidityAParser.EnumDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#parameterList.
    def enterParameterList(self, ctx:SolidityAParser.ParameterListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#parameterList.
    def exitParameterList(self, ctx:SolidityAParser.ParameterListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#parameter.
    def enterParameter(self, ctx:SolidityAParser.ParameterContext):
        pass

    # Exit a parse tree produced by SolidityAParser#parameter.
    def exitParameter(self, ctx:SolidityAParser.ParameterContext):
        pass


    # Enter a parse tree produced by SolidityAParser#eventParameterList.
    def enterEventParameterList(self, ctx:SolidityAParser.EventParameterListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#eventParameterList.
    def exitEventParameterList(self, ctx:SolidityAParser.EventParameterListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#eventParameter.
    def enterEventParameter(self, ctx:SolidityAParser.EventParameterContext):
        pass

    # Exit a parse tree produced by SolidityAParser#eventParameter.
    def exitEventParameter(self, ctx:SolidityAParser.EventParameterContext):
        pass


    # Enter a parse tree produced by SolidityAParser#functionTypeParameterList.
    def enterFunctionTypeParameterList(self, ctx:SolidityAParser.FunctionTypeParameterListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#functionTypeParameterList.
    def exitFunctionTypeParameterList(self, ctx:SolidityAParser.FunctionTypeParameterListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#functionTypeParameter.
    def enterFunctionTypeParameter(self, ctx:SolidityAParser.FunctionTypeParameterContext):
        pass

    # Exit a parse tree produced by SolidityAParser#functionTypeParameter.
    def exitFunctionTypeParameter(self, ctx:SolidityAParser.FunctionTypeParameterContext):
        pass


    # Enter a parse tree produced by SolidityAParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:SolidityAParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by SolidityAParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:SolidityAParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by SolidityAParser#typeName.
    def enterTypeName(self, ctx:SolidityAParser.TypeNameContext):
        pass

    # Exit a parse tree produced by SolidityAParser#typeName.
    def exitTypeName(self, ctx:SolidityAParser.TypeNameContext):
        pass


    # Enter a parse tree produced by SolidityAParser#userDefinedTypeName.
    def enterUserDefinedTypeName(self, ctx:SolidityAParser.UserDefinedTypeNameContext):
        pass

    # Exit a parse tree produced by SolidityAParser#userDefinedTypeName.
    def exitUserDefinedTypeName(self, ctx:SolidityAParser.UserDefinedTypeNameContext):
        pass


    # Enter a parse tree produced by SolidityAParser#mappingKey.
    def enterMappingKey(self, ctx:SolidityAParser.MappingKeyContext):
        pass

    # Exit a parse tree produced by SolidityAParser#mappingKey.
    def exitMappingKey(self, ctx:SolidityAParser.MappingKeyContext):
        pass


    # Enter a parse tree produced by SolidityAParser#mapping.
    def enterMapping(self, ctx:SolidityAParser.MappingContext):
        pass

    # Exit a parse tree produced by SolidityAParser#mapping.
    def exitMapping(self, ctx:SolidityAParser.MappingContext):
        pass


    # Enter a parse tree produced by SolidityAParser#mappingKeyName.
    def enterMappingKeyName(self, ctx:SolidityAParser.MappingKeyNameContext):
        pass

    # Exit a parse tree produced by SolidityAParser#mappingKeyName.
    def exitMappingKeyName(self, ctx:SolidityAParser.MappingKeyNameContext):
        pass


    # Enter a parse tree produced by SolidityAParser#mappingValueName.
    def enterMappingValueName(self, ctx:SolidityAParser.MappingValueNameContext):
        pass

    # Exit a parse tree produced by SolidityAParser#mappingValueName.
    def exitMappingValueName(self, ctx:SolidityAParser.MappingValueNameContext):
        pass


    # Enter a parse tree produced by SolidityAParser#functionTypeName.
    def enterFunctionTypeName(self, ctx:SolidityAParser.FunctionTypeNameContext):
        pass

    # Exit a parse tree produced by SolidityAParser#functionTypeName.
    def exitFunctionTypeName(self, ctx:SolidityAParser.FunctionTypeNameContext):
        pass


    # Enter a parse tree produced by SolidityAParser#storageLocation.
    def enterStorageLocation(self, ctx:SolidityAParser.StorageLocationContext):
        pass

    # Exit a parse tree produced by SolidityAParser#storageLocation.
    def exitStorageLocation(self, ctx:SolidityAParser.StorageLocationContext):
        pass


    # Enter a parse tree produced by SolidityAParser#stateMutability.
    def enterStateMutability(self, ctx:SolidityAParser.StateMutabilityContext):
        pass

    # Exit a parse tree produced by SolidityAParser#stateMutability.
    def exitStateMutability(self, ctx:SolidityAParser.StateMutabilityContext):
        pass


    # Enter a parse tree produced by SolidityAParser#block.
    def enterBlock(self, ctx:SolidityAParser.BlockContext):
        pass

    # Exit a parse tree produced by SolidityAParser#block.
    def exitBlock(self, ctx:SolidityAParser.BlockContext):
        pass


    # Enter a parse tree produced by SolidityAParser#statement.
    def enterStatement(self, ctx:SolidityAParser.StatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#statement.
    def exitStatement(self, ctx:SolidityAParser.StatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#expressionStatement.
    def enterExpressionStatement(self, ctx:SolidityAParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#expressionStatement.
    def exitExpressionStatement(self, ctx:SolidityAParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#ifStatement.
    def enterIfStatement(self, ctx:SolidityAParser.IfStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#ifStatement.
    def exitIfStatement(self, ctx:SolidityAParser.IfStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#tryStatement.
    def enterTryStatement(self, ctx:SolidityAParser.TryStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#tryStatement.
    def exitTryStatement(self, ctx:SolidityAParser.TryStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#catchClause.
    def enterCatchClause(self, ctx:SolidityAParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by SolidityAParser#catchClause.
    def exitCatchClause(self, ctx:SolidityAParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by SolidityAParser#whileStatement.
    def enterWhileStatement(self, ctx:SolidityAParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#whileStatement.
    def exitWhileStatement(self, ctx:SolidityAParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#simpleStatement.
    def enterSimpleStatement(self, ctx:SolidityAParser.SimpleStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#simpleStatement.
    def exitSimpleStatement(self, ctx:SolidityAParser.SimpleStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#uncheckedStatement.
    def enterUncheckedStatement(self, ctx:SolidityAParser.UncheckedStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#uncheckedStatement.
    def exitUncheckedStatement(self, ctx:SolidityAParser.UncheckedStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#forStatement.
    def enterForStatement(self, ctx:SolidityAParser.ForStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#forStatement.
    def exitForStatement(self, ctx:SolidityAParser.ForStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#inlineAssemblyStatement.
    def enterInlineAssemblyStatement(self, ctx:SolidityAParser.InlineAssemblyStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#inlineAssemblyStatement.
    def exitInlineAssemblyStatement(self, ctx:SolidityAParser.InlineAssemblyStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#inlineAssemblyStatementFlag.
    def enterInlineAssemblyStatementFlag(self, ctx:SolidityAParser.InlineAssemblyStatementFlagContext):
        pass

    # Exit a parse tree produced by SolidityAParser#inlineAssemblyStatementFlag.
    def exitInlineAssemblyStatementFlag(self, ctx:SolidityAParser.InlineAssemblyStatementFlagContext):
        pass


    # Enter a parse tree produced by SolidityAParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:SolidityAParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:SolidityAParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#continueStatement.
    def enterContinueStatement(self, ctx:SolidityAParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#continueStatement.
    def exitContinueStatement(self, ctx:SolidityAParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#breakStatement.
    def enterBreakStatement(self, ctx:SolidityAParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#breakStatement.
    def exitBreakStatement(self, ctx:SolidityAParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#returnStatement.
    def enterReturnStatement(self, ctx:SolidityAParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#returnStatement.
    def exitReturnStatement(self, ctx:SolidityAParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#throwStatement.
    def enterThrowStatement(self, ctx:SolidityAParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#throwStatement.
    def exitThrowStatement(self, ctx:SolidityAParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#emitStatement.
    def enterEmitStatement(self, ctx:SolidityAParser.EmitStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#emitStatement.
    def exitEmitStatement(self, ctx:SolidityAParser.EmitStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#revertStatement.
    def enterRevertStatement(self, ctx:SolidityAParser.RevertStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#revertStatement.
    def exitRevertStatement(self, ctx:SolidityAParser.RevertStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#variableDeclarationStatement.
    def enterVariableDeclarationStatement(self, ctx:SolidityAParser.VariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by SolidityAParser#variableDeclarationStatement.
    def exitVariableDeclarationStatement(self, ctx:SolidityAParser.VariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by SolidityAParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx:SolidityAParser.VariableDeclarationListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx:SolidityAParser.VariableDeclarationListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#identifierList.
    def enterIdentifierList(self, ctx:SolidityAParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#identifierList.
    def exitIdentifierList(self, ctx:SolidityAParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#elementaryTypeName.
    def enterElementaryTypeName(self, ctx:SolidityAParser.ElementaryTypeNameContext):
        pass

    # Exit a parse tree produced by SolidityAParser#elementaryTypeName.
    def exitElementaryTypeName(self, ctx:SolidityAParser.ElementaryTypeNameContext):
        pass


    # Enter a parse tree produced by SolidityAParser#expression.
    def enterExpression(self, ctx:SolidityAParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#expression.
    def exitExpression(self, ctx:SolidityAParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:SolidityAParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:SolidityAParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#expressionList.
    def enterExpressionList(self, ctx:SolidityAParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#expressionList.
    def exitExpressionList(self, ctx:SolidityAParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#nameValueList.
    def enterNameValueList(self, ctx:SolidityAParser.NameValueListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#nameValueList.
    def exitNameValueList(self, ctx:SolidityAParser.NameValueListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#nameValue.
    def enterNameValue(self, ctx:SolidityAParser.NameValueContext):
        pass

    # Exit a parse tree produced by SolidityAParser#nameValue.
    def exitNameValue(self, ctx:SolidityAParser.NameValueContext):
        pass


    # Enter a parse tree produced by SolidityAParser#functionCallArguments.
    def enterFunctionCallArguments(self, ctx:SolidityAParser.FunctionCallArgumentsContext):
        pass

    # Exit a parse tree produced by SolidityAParser#functionCallArguments.
    def exitFunctionCallArguments(self, ctx:SolidityAParser.FunctionCallArgumentsContext):
        pass


    # Enter a parse tree produced by SolidityAParser#functionCall.
    def enterFunctionCall(self, ctx:SolidityAParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by SolidityAParser#functionCall.
    def exitFunctionCall(self, ctx:SolidityAParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyBlock.
    def enterAssemblyBlock(self, ctx:SolidityAParser.AssemblyBlockContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyBlock.
    def exitAssemblyBlock(self, ctx:SolidityAParser.AssemblyBlockContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyItem.
    def enterAssemblyItem(self, ctx:SolidityAParser.AssemblyItemContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyItem.
    def exitAssemblyItem(self, ctx:SolidityAParser.AssemblyItemContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyExpression.
    def enterAssemblyExpression(self, ctx:SolidityAParser.AssemblyExpressionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyExpression.
    def exitAssemblyExpression(self, ctx:SolidityAParser.AssemblyExpressionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyMember.
    def enterAssemblyMember(self, ctx:SolidityAParser.AssemblyMemberContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyMember.
    def exitAssemblyMember(self, ctx:SolidityAParser.AssemblyMemberContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyCall.
    def enterAssemblyCall(self, ctx:SolidityAParser.AssemblyCallContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyCall.
    def exitAssemblyCall(self, ctx:SolidityAParser.AssemblyCallContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyLocalDefinition.
    def enterAssemblyLocalDefinition(self, ctx:SolidityAParser.AssemblyLocalDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyLocalDefinition.
    def exitAssemblyLocalDefinition(self, ctx:SolidityAParser.AssemblyLocalDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyAssignment.
    def enterAssemblyAssignment(self, ctx:SolidityAParser.AssemblyAssignmentContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyAssignment.
    def exitAssemblyAssignment(self, ctx:SolidityAParser.AssemblyAssignmentContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyIdentifierOrList.
    def enterAssemblyIdentifierOrList(self, ctx:SolidityAParser.AssemblyIdentifierOrListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyIdentifierOrList.
    def exitAssemblyIdentifierOrList(self, ctx:SolidityAParser.AssemblyIdentifierOrListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyIdentifierList.
    def enterAssemblyIdentifierList(self, ctx:SolidityAParser.AssemblyIdentifierListContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyIdentifierList.
    def exitAssemblyIdentifierList(self, ctx:SolidityAParser.AssemblyIdentifierListContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyStackAssignment.
    def enterAssemblyStackAssignment(self, ctx:SolidityAParser.AssemblyStackAssignmentContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyStackAssignment.
    def exitAssemblyStackAssignment(self, ctx:SolidityAParser.AssemblyStackAssignmentContext):
        pass


    # Enter a parse tree produced by SolidityAParser#labelDefinition.
    def enterLabelDefinition(self, ctx:SolidityAParser.LabelDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#labelDefinition.
    def exitLabelDefinition(self, ctx:SolidityAParser.LabelDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblySwitch.
    def enterAssemblySwitch(self, ctx:SolidityAParser.AssemblySwitchContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblySwitch.
    def exitAssemblySwitch(self, ctx:SolidityAParser.AssemblySwitchContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyCase.
    def enterAssemblyCase(self, ctx:SolidityAParser.AssemblyCaseContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyCase.
    def exitAssemblyCase(self, ctx:SolidityAParser.AssemblyCaseContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyFunctionDefinition.
    def enterAssemblyFunctionDefinition(self, ctx:SolidityAParser.AssemblyFunctionDefinitionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyFunctionDefinition.
    def exitAssemblyFunctionDefinition(self, ctx:SolidityAParser.AssemblyFunctionDefinitionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyFunctionReturns.
    def enterAssemblyFunctionReturns(self, ctx:SolidityAParser.AssemblyFunctionReturnsContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyFunctionReturns.
    def exitAssemblyFunctionReturns(self, ctx:SolidityAParser.AssemblyFunctionReturnsContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyFor.
    def enterAssemblyFor(self, ctx:SolidityAParser.AssemblyForContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyFor.
    def exitAssemblyFor(self, ctx:SolidityAParser.AssemblyForContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyIf.
    def enterAssemblyIf(self, ctx:SolidityAParser.AssemblyIfContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyIf.
    def exitAssemblyIf(self, ctx:SolidityAParser.AssemblyIfContext):
        pass


    # Enter a parse tree produced by SolidityAParser#assemblyLiteral.
    def enterAssemblyLiteral(self, ctx:SolidityAParser.AssemblyLiteralContext):
        pass

    # Exit a parse tree produced by SolidityAParser#assemblyLiteral.
    def exitAssemblyLiteral(self, ctx:SolidityAParser.AssemblyLiteralContext):
        pass


    # Enter a parse tree produced by SolidityAParser#tupleExpression.
    def enterTupleExpression(self, ctx:SolidityAParser.TupleExpressionContext):
        pass

    # Exit a parse tree produced by SolidityAParser#tupleExpression.
    def exitTupleExpression(self, ctx:SolidityAParser.TupleExpressionContext):
        pass


    # Enter a parse tree produced by SolidityAParser#numberLiteral.
    def enterNumberLiteral(self, ctx:SolidityAParser.NumberLiteralContext):
        pass

    # Exit a parse tree produced by SolidityAParser#numberLiteral.
    def exitNumberLiteral(self, ctx:SolidityAParser.NumberLiteralContext):
        pass


    # Enter a parse tree produced by SolidityAParser#identifier.
    def enterIdentifier(self, ctx:SolidityAParser.IdentifierContext):
        pass

    # Exit a parse tree produced by SolidityAParser#identifier.
    def exitIdentifier(self, ctx:SolidityAParser.IdentifierContext):
        pass


    # Enter a parse tree produced by SolidityAParser#hexLiteral.
    def enterHexLiteral(self, ctx:SolidityAParser.HexLiteralContext):
        pass

    # Exit a parse tree produced by SolidityAParser#hexLiteral.
    def exitHexLiteral(self, ctx:SolidityAParser.HexLiteralContext):
        pass


    # Enter a parse tree produced by SolidityAParser#overrideSpecifier.
    def enterOverrideSpecifier(self, ctx:SolidityAParser.OverrideSpecifierContext):
        pass

    # Exit a parse tree produced by SolidityAParser#overrideSpecifier.
    def exitOverrideSpecifier(self, ctx:SolidityAParser.OverrideSpecifierContext):
        pass


    # Enter a parse tree produced by SolidityAParser#stringLiteral.
    def enterStringLiteral(self, ctx:SolidityAParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SolidityAParser#stringLiteral.
    def exitStringLiteral(self, ctx:SolidityAParser.StringLiteralContext):
        pass



del SolidityAParser